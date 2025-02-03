# QRGen

## Project Goal

The goal of this project is to build an open source QR code generator that is completely free to use—without any paywalls or account logins. The vision is that, over time, advertisements will help cover the infrastructure costs, ensuring that all community-developed features remain accessible for free. While a paid login option may be introduced in the future to support additional functionalities (such as hosting QR codes), **nothing developed by the open source community will ever be hidden behind a paywall.**

## Overview

QRgen Backend is a serverless QR code generator built with AWS Lambda and API Gateway, complemented by a simple HTML/JavaScript frontend. The system dynamically creates a QR code image for any provided URL and returns it as a base64-encoded string in a JSON response.

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Features](#features)
- [Backend Overview](#backend-overview)
- [Frontend Overview](#frontend-overview)
- [Setup and Deployment](#setup-and-deployment)
  - [AWS Lambda & API Gateway](#aws-lambda--api-gateway)
  - [CI/CD with GitHub Actions](#cicd-with-github-actions)
  - [Custom Domain & Cloudflare (Optional)](#custom-domain--cloudflare-optional)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Architecture

- **AWS Lambda:**  
  The backend function uses Python along with the qrcode library and Pillow for image processing. It processes incoming requests, generates the QR code, encodes it in base64, and returns the result.

- **API Gateway:**  
  An HTTP API Gateway route is configured to accept GET requests. The route (e.g., `/generate`) is integrated with the Lambda function, allowing external clients to trigger the QR code generation.

- **Frontend:**  
  A static HTML page built with Bootstrap provides a user interface. JavaScript on the page collects user input, calls the API Gateway endpoint, and displays the resulting QR code image.

- **CI/CD:**  
  GitHub Actions workflows are set up to deploy updates to both the S3-hosted frontend and the Lambda function automatically when code is pushed to the `main` branch.

## Features

- **Serverless Architecture:** Built entirely on AWS Lambda and API Gateway.
- **Dynamic QR Code Generation:** Generates QR codes on-demand from user-specified URLs.
- **Responsive Frontend:** A Bootstrap-based HTML interface provides a user-friendly experience.
- **Automated Deployment:** CI/CD pipeline using GitHub Actions for automatic updates.
- **CORS Support:** Configured to allow cross-origin requests for frontend integration.

## Backend Overview

The backend is implemented in Python. The Lambda function performs the following steps:
- Extracts the URL from the incoming query string parameters.
- Validates the URL input.
- Generates a QR code using the qrcode library.
- Processes the generated image using Pillow.
- Encodes the image in base64.
- Returns a JSON response containing the QR code data.

## Frontend Overview

The frontend consists of a single HTML page that:
- Uses Bootstrap for responsive design.
- Provides a form for users to input a URL.
- Uses JavaScript (with the Fetch API) to call the API Gateway endpoint.
- Displays the base64-encoded QR code image returned from the backend.

## Setup and Deployment

### AWS Lambda & API Gateway

1. **Backend Deployment:**  
   - Package the backend code along with its dependencies (ensuring the package is built in a Linux environment for compatibility with AWS Lambda).
   - Deploy the package to AWS Lambda via the AWS Console, CLI, or your CI/CD pipeline.
   - Configure API Gateway to route requests (using a GET method at the `/generate` path) to your Lambda function.

2. **Frontend Deployment:**  
   - Host the static HTML file (and related assets) on an S3 bucket configured for static website hosting.
   - Optionally, front your S3 bucket with CloudFront and use Cloudflare for added performance and security.

### CI/CD with GitHub Actions

- **Automated Deployments:**  
  GitHub Actions workflows are set up to automatically build and deploy the Lambda function and update the S3 bucket hosting your frontend whenever changes are pushed to the `main` branch.
- **Workflow Files:**  
  - Check out your code.
  - Set up Python and install dependencies.
  - Package the Lambda function.
  - Deploy the function via the AWS CLI.
  - Deploy your frontend to S3 (if applicable).

### Custom Domain & Cloudflare (Optional)

- **Custom Domains:**  
  Use CloudFront with a custom domain for your S3-hosted frontend and configure API Gateway with a custom domain for your API.
- **SSL/TLS:**  
  Attach trusted certificates (via ACM) for your custom domains and set up the proper DNS records in Cloudflare.

## Testing

1. **Lambda Function:**  
   Test your Lambda function directly in the AWS Console by creating a test event with a URL parameter. Ensure the function returns a status code of 200 and a valid `qr_code` string.

2. **API Gateway Endpoint:**  
   Use tools like cURL, Postman, or a browser to call the API Gateway URL (for example, by appending `?url=https://example.com` to the endpoint) and verify the JSON response.

3. **Frontend:**  
   Open your deployed HTML page, input a URL, and click the "Generate QR Code" button. Verify that the QR code appears correctly on the page.

## Contributing

Contributions are welcome! If you wish to contribute:
- Fork the repository and create your branch from `main`.
- Follow standard coding practices and include tests where applicable.
- Submit a pull request with a clear description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
