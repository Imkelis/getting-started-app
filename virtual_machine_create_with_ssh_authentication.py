from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

def main():
    client = ComputeManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="bb4f2673-5471-4327-a067-1715eb7145c3",  # Replace with your actual subscription ID
    )

    response = client.virtual_machines.begin_create_or_update(
        resource_group_name="lab4",
        vm_name="vmLab4",
        parameters={
            "location": "uksouth",
            "properties": {
                "hardwareProfile": {"vmSize": "Standard_D1_v2"},
                "networkProfile": {
                    "networkInterfaces": [
                        {
                            "id": "/subscriptions/bb4f2673-5471-4327-a067-1715eb7145c3/resourceGroups/lab4/providers/Microsoft.Network/networkInterfaces/nic4",
                            "properties": {"primary": True},
                        }
                    ]
                },
                "osProfile": {
                    "adminUsername": "paul",
                    "computerName": "vmLab4",
                    "linuxConfiguration": {
                        "disablePasswordAuthentication": True,
                        "ssh": {
                            "publicKeys": [
                                {
                                    "keyData": """ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCvVVTbwV18CX2jwTreWitAH+N8s4GT2ll8jGh58G11igelRC1LDEhzKuYtenBVHsLUBqtNzgovVlJBhy/GDHhzABpwjfCwdiq2MpvaVVGumKqW1rKUFmfF28M0sBz4+QBNwvBwr63hm2yxRDbrvBU2xQAZyFXPS5eMwNfzCIew/ZQvJR4tALyhAnj8GJuiylke/sR4tCDN4yLlzUhxp5AUjtBgyn5DAK0MQuQN9TfVLqnXsoChbPb2MBFGt401TN+qTc2/k7EQccp3S3LmK3aql01PSMt8I00hbsFJjY96xN5dh0mWNN1RR4IHHZygQ/gn/FmSXobQS93ElaliPs9MIHxn57/nHbkgH0RpDBjHg8JIm0ook5Pe/6pEj1Ts6kukZVRtvNFQ/xskbJO22x3/FRWxpQ+6fHEoq6NeU/FcC6C6cXCS7wOXGNOccjWuDD0xC8psb2HrFrl7E5BqmeSBBhKGWV6778j5ydeKlAFJqdFCP66Yr0dAREiSseDxOhJs6ZCjZ+adRJN3X8ZpqFTdCN0hIXroosTtfOH/1Lke+sqxdae07aQvNjR0B4Kn/ybRUExAIoYtjAGh2IcCLPUtUvFvc7js7o6YEgImBXONsUxukgfpVH984H2gKSYq5y+5rLn4FYjaJAujc3yudmZmto6sXM4uN+2DNRE39ThkYQ== Ignas@IgnasLaptop
 """,
                                    "path": "/home/paul/.ssh/authorized_keys",
                                }
                            ]
                        },
                    },
                },
                "storageProfile": {
                    "imageReference": {
                        "offer": "UbuntuServer",
                        "publisher": "Canonical",
                        "sku": "16.04-LTS",
                        "version": "latest",
                    },
                },
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/compute/resource-manager/Microsoft.Compute/ComputeRP/stable/2023-07-01/examples/virtualMachineExamples/VirtualMachine_Create_WithSshAuthentication.json
if __name__ == "__main__":
    main()
