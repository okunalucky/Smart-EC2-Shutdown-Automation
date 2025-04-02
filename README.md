
<h2>Smart EC2 Shutdown Automation</h2>
<h2>Introduction</h2>
<p>In the era of cloud computing, optimizing resource usage is crucial for cost management and operational efficiency. This project explores the use of AWS Lambda, a serverless compute service, to automatically shut down EC2 instances that exceed the t2.medium instance type. By implementing this solution, organizations can effectively manage their cloud resources, reduce unnecessary costs, and maintain better control over their computing environments.</p>
<h2>Prerequisites</h2>
<p>
Before starting this project, ensure you have the following:
<li>AWS Account: An active AWS account with sufficient permissions to create Lambda functions, manage EC2 instances, and access CloudWatch.</li>
<li>Basic Knowledge of AWS Services: Familiarity with AWS Lambda, EC2 instances, IAM roles, and CloudWatch Events.</li>
<li>AWS CLI or Management Console: Access to the AWS Management Console or AWS CLI to configure and manage resources.</li>
<li>IAM Role: An IAM role with permissions to describe EC2 instances and stop them, which the Lambda function will assume.</li>
<li>Basic Understanding of Python or Node.js: Familiarity with the programming language you choose to write the Lambda function.</li></p>
<h2>Use Cases</h2>
<p>
Leveraging AWS Lambda to manage EC2 instances can be beneficial in various scenarios, including:
<li>Cost Management: Automatically shutting down instances that are not required, helping to reduce monthly cloud expenditure.</li>
<li>Resource Optimization: Ensuring that only necessary instances are running, which can improve overall resource utilization.</li>
<li>Automated Compliance: Enforcing organizational policies that limit the usage of certain instance types, ensuring compliance with cost management strategies.</li>
<li>Scheduled Maintenance: Implementing scheduled functions that shut down instances during non-peak hours to save costs.</li>
<li>Development and Testing: Quickly managing instances in development and testing environments, ensuring that resources are only active when needed.</li></p>
<h2>Steps</h2>
<p><li>You start by imorting boto3 on vscode</li></p>
<p><li>Define the minimum instance type</li></p>
<p><li>go to instance boto 3 documentation to get a list of all the instance type and also use amazon q to do the sorting</li></p>
<p><li>Use a for loop to define the instance id</li></p>
<p><li>define the lamba function and process to your aws console to create a trigger</li></p>
<p><li>refer to the .py files attached to see the code used</li></p>
      

