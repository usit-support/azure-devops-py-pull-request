# Introduction 
Introducing our premier Azure DevOps Extension, the 'Auto PR Manager'. This robust extension is designed to streamline your workflow by automatically creating or updating Pull Requests within Azure Pipelines using your GIT repository.

Leveraging Azure Pipelines, Auto PR Manager allows you to stay focused on your code while it takes care of the complexities of PR management. This extension is meticulously designed to foster seamless interaction with your GIT repositories, ensuring real-time synchronization and seamless workflow integration.

The Auto PR Manager is your key to efficient code reviews and collaborative coding. It promptly creates Pull Requests when new commits are made, keeping your team on the same page. In case of ongoing Pull Requests, the extension intelligently updates them, preventing duplicate requests and saving valuable time.

Furthermore, the Auto PR Manager guarantees optimal compliance with your development strategies by adhering to branch policies and safeguards your code base from conflicting changes. Empower your development process with this comprehensive tool, designed for both novice users and seasoned professionals alike.

Experience a new standard in automated PR management with the Auto PR Manager, your first step towards a smarter, more productive DevOps journey.

# Getting Started
TODO: Here are the steps to install an Azure DevOps extension in your organization:
1.	Log in to Azure DevOps: First, navigate to the Azure DevOps portal and sign in to your account.

2.	Open Organization Settings: From your organization's home page, click on the "Organization settings" option located at the bottom of the left-hand panel.

3.	Access Extensions: Select "Extensions" from the menu under the "General" category.

4.	Browse Marketplace: Click on "Browse Marketplace" which will open a new tab leading you to the Visual Studio Marketplace.

5.	Find your Extension: Use the search bar to find the extension you want to install. For instance, if you're installing the 'Auto PR Manager', type in the name and hit enter.

6.	Install the Extension: Click on the extension from the search results to open its details page. Here, click on the "Get it free" button. This will prompt a window to select the organization you wish to install this extension for.

7.	Select Organization and Confirm: Choose your organization from the dropdown list and click on "Install".

8.	Verify Installation: You will be redirected back to Azure DevOps. Under "Extensions", you should now see the installed extension. You may need to refresh the page to see the new extension.

Remember, you must have the necessary permissions in your organization to install extensions. If you don't, you'll need to request the installation from someone who does have these permissions.

# Build and Test
1.	Log in to Azure DevOps: Navigate to the Azure DevOps portal and sign in to your account.

2.	Navigate to Pipelines: From your organization's home page, select your project. Then, click on "Pipelines" in the left-hand panel.

3.	Create Pipeline: Click on the "Create Pipeline" button to start the pipeline creation process.

4.	Select Repository: Since your source type is 'Azure Repos Git', select that option. Then, you'll need to choose the specific repository that contains your 'azure-pipelines.yml' file.

5.	Configure Your Pipeline: Choose the 'YAML' configuration option, indicating you'll be using a YAML file to set up your pipeline.

6.	Select YAML File: You'll be asked for the path to your YAML file within your repository. Since your file is named 'azure-pipelines.yml', input that into the path and Azure DevOps will display the content of your YAML file for review.

7.	Run and Save: Finally, click the "Run" button to validate and immediately run your pipeline, or "Save" if you wish to simply make the pipeline available without running it at this time.

Remember, the user creating the pipeline must have enough permissions to access the repository and create pipelines. If you don't see the repository you expect, or encounter permission issues, reach out to your organization's Azure DevOps administrator.

# Contribute
TODO: Explain how other users and developers can contribute to make your code better. 

If you want to learn more about creating good readme files then refer the following [guidelines](https://docs.microsoft.com/en-us/azure/devops/repos/git/create-a-readme?view=azure-devops). You can also seek inspiration from the below readme files:
- [Visual Studio Code](https://github.com/Microsoft/vscode)