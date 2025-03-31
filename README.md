
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
