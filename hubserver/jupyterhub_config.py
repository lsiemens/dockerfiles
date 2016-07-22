import os
import subprocess
config = get_config()

# Use GitHub OAuth to authenticate users
config.JupyterHub.authenticator_class = 'oauthenticator.GitHubOAuthenticator'
config.GitHubOAuthenticator.oauth_callback_url = 'https://206.12.96.12/hub/oauth_callback'
config.GitHubOAuthenticator.client_id = 'a4b7e7154c6f9d8497fc'
config.GitHubOAuthenticator.client_secret = '83784c5306df793900143b8d44aef24a379041ce'

# set of usernames of admin users
config.Authenticator.admin_users = ["fherwig", "syang", "lsiemens"]
config.Authenticator.whitelist = config.Authenticator.admin_users

# Spawn users in dockers
network_name = os.environ["DOCKER_NETWORK_NAME"]
hub_ip = os.environ["DOCKER_MACHINE_NAME"]
config.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
config.DockerSpawner.container_image = "lsiemens/singleuser"
config.DockerSpawner.use_internal_ip = True
config.DockerSpawner.network_name = network_name
config.DockerSpawner.extra_host_config = {"network_mode":network_name}
config.DockerSpawner.extra_start_kwargs = {"network_mode":network_name}
config.DockerSpawner.remove_containers = True
config.DockerSpawner.hub_ip_connect = hub_ip

# the docker instances need to access the HUB                                             
config.JupyterHub.hub_ip = hub_ip
config.JupyterHub.hub_port = 8000

# ussing ssl so set to 443
config.JupyterHub.port = 443
config.JupyterHub.ssl_cert = '/srv/jupyterhub/SSL/ssl.crt'
config.JupyterHub.ssl_key = '/srv/jupyterhub/SSL/ssl.key'

# make cookie secret and auth token
cookie = subprocess.Popen(["openssl", "rand", "2049"], stdout=subprocess.PIPE)
token = subprocess.Popen(["openssl", "rand", "-hex", "129"], stdout=subprocess.PIPE)
config.JupyterHub.cookie_secret = cookie.communicate()[0][:-1]
config.JupyterHub.proxy_auth_token = token.communicate()[0][:-1]

data_mount_point = os.environ.get("DATA_VOLUME")
config.JupyterHub.db_url = os.path.join("sqlite:///", data_mount_point, "jupyterhub.sqlite")
print(config.JupyterHub.db_url)
