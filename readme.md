##  JumpCloud AutoPkg Importer

![relax and automate your software deployments](https://github.com/TheJumpCloud/JC-AutoPkg-Importer/wiki/images/mac-management-transparent.png)

JumpCloud can leverage [AutoPkg](https://github.com/autopkg/autopkg) to automate package testing and deployment through the JumpCloud AutoPkg Importer. Those familiar with AutoPkg can use develop their own .pkg overrides which invoke JumpCloud AutoPkg Importer processor. To learn more about AutoPkg, visit the [AutoPkg wiki](https://github.com/autopkg/autopkg/wiki) page for documentation. The JumpCloud AutoPkg Importer was designed to process AutoPkg packages, upload them to distribution points and dynamically create JumpCloud commands and groups.

Installation documentation and usage can be found on the [JumpCloud AutoPkg Importer wiki](https://github.com/TheJumpCloud/JC-AutoPkg-Importer/wiki).

## At a glance

The JumpCloud AutoPkg Importer is an [AutoPkg recipe processor](https://github.com/autopkg/autopkg/wiki/Processor-Locations) designed to help automate software deployments and updates.

This processor is in early access, meaning functionality many change over time. The JC-AutoPkg-Importer uses Amazon Web Services S3 Buckets to store .pkg files and the JumpCloud APIs to generate dynamic commands which link to the objects stored in S3.

![autopkg workflow](https://github.com/TheJumpCloud/JC-AutoPkg-Importer/wiki/images/AutoPkg%20Diagram.png)

In general the intended use of this processor is to enable the following workflow:

Software .pkg files are generated from AuoPkg Recipes. That software package is uploaded to an AWS S3 Bucket for storage a link to that bucket object is then generated. A dynamic group and command are generated in JumpCloud. The dynamic JumpCloud system group contains systems that don't have or require the updated version of that software package. The dynamic JumpCloud command targets the system group and installs the software package uploaded to the AWS S3 Bucket. The command is run and JumpCloud systems install the latest version of the software package.
