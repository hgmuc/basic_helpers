import pytest
from unittest.mock import MagicMock, patch
from basic_helpers.google_drive import download_file_from_google_drive

def test_download_direct_no_warning(tmp_path):
    """Test successful download when no virus warning is present."""
    dest = tmp_path / "test.txt"
    file_id = "123"
    
    with patch("requests.Session") as mock_session_cls:
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.text = "Direct download content"
        mock_response.iter_content.return_value = [b"data_chunk"]
        mock_session.get.return_value = mock_response
        
        download_file_from_google_drive(file_id, str(dest))
        
        assert dest.read_bytes() == b"data_chunk"
        # Check that it only called GET once (no redirect/warning flow)
        assert mock_session.get.call_count == 1

def test_download_with_virus_warning(tmp_path):
    """Test the two-step download flow when a virus warning page appears."""
    dest = tmp_path / "test.txt"
    file_id = "123"
    
    # Mock HTML response for the warning page
    warning_html = """
    <html>
        <body>
            Google Drive - Virus scan warning
            <input name="confirm" value="t_123">
            <input name="uuid" value="u_456">
        </body>
    </html>
    """
    
    with patch("requests.Session") as mock_session_cls:
        mock_session = mock_session_cls.return_value
        
        # First response: The warning page
        mock_resp1 = MagicMock()
        mock_resp1.text = warning_html
        
        # Second response: The actual file stream
        mock_resp2 = MagicMock()
        mock_resp2.iter_content.return_value = [b"file_content"]
        
        # Configure the mock session to return resp1 then resp2
        mock_session.get.side_effect = [mock_resp1, mock_resp2]
        
        download_file_from_google_drive(file_id, str(dest))
        
        # Verify calls
        assert mock_session.get.call_count == 2
        args, kwargs = mock_session.get.call_args # Check second call params
        assert kwargs['params']['confirm'] == "t_123"
        assert kwargs['params']['uuid'] == "u_456"
        assert dest.read_bytes() == b"file_content"


@pytest.mark.integration
def test_download_real_file(tmp_path):
    """Integration test with a real Google Drive ID."""
    file_id = '1Xd5KOUx_vQA-OI6fcmVYe2a2S2sFNmmx'
    #destination = tmp_path / "downloaded_file.bin"
    destination = tmp_path / "sample.md"
    
    # Execute
    download_file_from_google_drive(file_id, str(destination))
    
    # Verification
    assert destination.exists()
    assert destination.stat().st_size > 0
    
    # Clean up (tmp_path handles this automatically, but for clarity:)
    print(f"\nIntegration test file downloaded to: {destination}")
