# The name of the dashboard to be added to HORIZON['dashboards']. Required.
DASHBOARD = 'mydashboard'# this must have the same name as the directory which was created in the previous step

# If set to True, this dashboard will not be added to the settings.
DISABLED = False

# A list of applications to be added to INSTALLED_APPS.
ADD_INSTALLED_APPS = [
'openstack_dashboard.dashboards.mydashboard', # this too must refer to the directory of the created in the previous step
]