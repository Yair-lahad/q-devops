# save as permission_discovery.py
import boto3
import botocore

def test_service_access():
    # Services commonly used in DevOps
    services_to_check = [
        'ec2', 'lambda', 'ecs', 'eks', 'cloudformation', 
        'codebuild', 'codepipeline', 'ecr', 'logs',
        'cloudwatch', 'apigateway', 'dynamodb', 'rds'
    ]
    
    for service in services_to_check:
        try:
            # Just create a client - we'll try a simple list operation
            client = boto3.client(service)
            # Each service has different "list" operations - we'll try common ones
            if service == 'ec2':
                client.describe_regions()
                print(f"✓ {service}: Can access describe_regions")
            elif service == 'lambda':
                client.list_functions(MaxItems=1)
                print(f"✓ {service}: Can access list_functions")
            elif service == 'dynamodb':
                client.list_tables(Limit=1)
                print(f"✓ {service}: Can access list_tables")
            else:
                # Generic message when we can create a client but haven't tested operations
                print(f"? {service}: Client created, but operations not tested")
        except botocore.exceptions.ClientError as e:
            error = str(e)
            if "AccessDenied" in error or "UnauthorizedOperation" in error:
                print(f"✗ {service}: Access denied")
            else:
                print(f"! {service}: Error - {e}")
        except Exception as e:
            print(f"! {service}: Unexpected error - {e}")

if __name__ == "__main__":
    print("AWS Service Access Discovery")
    print("---------------------------")
    test_service_access()