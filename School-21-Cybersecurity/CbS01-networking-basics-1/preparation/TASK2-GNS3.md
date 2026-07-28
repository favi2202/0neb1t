# CbS1 Task 2 — GNS3 preparation runbook

Status: **Prepared; execution pending**.

## Goal

Create a GNS3 project containing an imported Cisco 3745 router. The official Cisco image and School 21 GitLab repository are not currently available, so no installation or successful import is claimed.

## Required resources

- GNS3
- An authorized Cisco 3745 IOS image supplied or approved by School 21
- The assigned project repository
- Sufficient local CPU/RAM/disk space

Do not download IOS images from random sources. They may be unlicensed, modified, or unsafe.

## Steps to perform later

1. Install/open GNS3.
2. Create a new blank project with a clear name such as `CbS1`.
3. Open the appliance/Dynamips IOS-router preferences. The exact menu wording can vary by GNS3 version.
4. Add a new IOS router and select the authorized Cisco 3745 image.
5. Confirm the detected platform is Cisco 3745 and accept or adjust the recommended RAM.
6. Finish the template wizard.
7. Drag one Cisco 3745 router onto the project canvas.
8. Start the router and open its console.
9. Verify that it boots and identify the model/version with:
   ```text
   enable
   show version
   ```
10. Save the device configuration:
    ```text
    copy running-config startup-config
    ```
11. Save and close the GNS3 project, reopen it, and confirm the router remains present.

On Linux, the README specifically mentions making `/usr/bin/dumpcap` executable and warns against installing GNS3 as a systemd service. Do not change dumpcap permissions unless packet capture actually fails and the change is appropriate for the local system.

## Expected result

- The project opens without missing-file errors.
- One Cisco 3745 router is visible.
- The router starts and its console is accessible.
- `show version` identifies the expected platform.
- The project is saved in the required repository location.

## Evidence to capture

1. Full GNS3 window showing project name and Cisco 3745 node.
2. Console showing the relevant lines from `show version`.
3. Project folder/file visible under `src`.
4. Later, GitLab `develop` branch showing the uploaded project.

Suggested screenshot names:

- `task2_gns3_topology.png`
- `task2_cisco_show_version.png`
- `task2_project_files.png`

## Troubleshooting

- **Router fails to start:** verify the image is valid for Dynamips and the configured platform/RAM is correct.
- **High CPU:** calculate/apply an Idle-PC value if the selected IOS requires it.
- **Console does not open:** check the configured console application and local firewall.
- **Packet capture later fails:** verify Wireshark/dumpcap/Npcap installation and permissions.
- **Project opens with missing files:** keep the image/template available locally and avoid moving project dependencies mid-task.

## Peer-review answers

- **Why GNS3?** It emulates network devices and allows realistic IOS configuration and packet capture.
- **Why save startup-config?** Running configuration is volatile; startup configuration persists after reload.
- **What proves the image works?** Successful boot plus `show version` output identifying the router platform.