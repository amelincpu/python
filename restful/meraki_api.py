import meraki

api_key = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
dashboard = meraki.DashboardAPI(api_key)

response = dashboard.organizations.getOrganizations()

for org in response:
    print('ID:{} Name:{}'.format(org['id'], org['name']))

response1 = dashboard.organizations.getOrganizationNetworks(organizationId=549236)
for net in response1:
    print('ID:{} Name{}'.format(net['id'], net['name']))