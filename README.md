Project Title:-Automated Static Website Deployment into Amazon S3 using Jenkins CI/CD and Automated CloudFront Cache Invalidation using AWS Lambda.




Project flow Diagram:-Developer------->GitHub------->Jenkins(CI/CD)------->Amazon S3------->AWS Lambda------->Amazon CloudFront------->Amazon Route53------->End Users.





AWS services used:-VPC,EC2,IAM,S3,lambda,cloudfront,route53,ACM
tools used:-git,github,jenkins





project summary:-
When developer pushes the code changes (HTML, CSS, JS) to the GitHub repository, a webhook automatically triggers the Jenkins pipeline. Jenkins then clones the latest code from GitHub and deploys the website files to the Amazon S3 bucket, excluding unnecessary files such as .git, README.md, Jenkinsfile and more. Once the files are updated in S3, they trigger an AWS Lambda function, which creates a CloudFront cache invalidation to ensure that the latest version of the website is served. CloudFront then distributes the updated content globally through its edge locations for faster access, while Route 53 maps the domain name to the CloudFront distribution. As a result, end users always see the most recent version of the website automatically, without any manual intervention, completing a fully automated CI/CD pipeline for static website deployment.