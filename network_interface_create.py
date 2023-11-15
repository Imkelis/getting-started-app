from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-network
# USAGE
    python network_interface_create.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="bb4f2673-5471-4327-a067-1715eb7145c3",
    )

    response = client.network_interfaces.begin_create_or_update(
        resource_group_name="lab4",
        network_interface_name="nic4",
        parameters={
            "location": "uksouth",
            "properties": {
                #"disableTcpStateTracking": True,
                "enableAcceleratedNetworking": True,
                "ipConfigurations": [
                    {
                        "name": "ipconfig1",
                        "properties": {
                            "publicIPAddress": {
                                "id": "/subscriptions/bb4f2673-5471-4327-a067-1715eb7145c3/resourceGroups/lab4/ providers/Microsoft.Network/publicIPAddresses/ip4"
                            },
                            "subnet": {
                                "id": "/subscriptions/bb4f2673-5471-4327-a067-1715eb7145c3/resourceGroups/lab4/ providers/Microsoft.Network/virtualNetworks/net4/subnets/snet4"
                            },
                        },
                    }
                ],
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/network/resource-manager/Microsoft.Network/stable/2023-05-01/examples/NetworkInterfaceCreate.json
if __name__ == "__main__":
    main()