
def test_service_status(ssh_client):
    output = ssh_client.run("systemctl status nginx")
    assert "active (running)" in output
