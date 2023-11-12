<p align="center">
  <a href="" rel="noopener">
 <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/294/pQ9YzVY.gif" alt="Postmortem"></a>
</p>
<h1 align="center">Post-Mortem Report</h1>

## Issue Summary

On November 1st 2023 at 11:37 AM, the company's website experienced an unexpected downtime that lasted for 17min. This incident resulted in a disruption of services and potential impact on user experience. Caused by a database server failure due to a sudden spike in traffic, exceeding the server's capacity.

## Timeline

- **11:37 AM** - Monitoring systems detected a sudden increase in server response times.
- **11:39 AM** - Users reported inability to access the website.
- **11:40 AM** - I initiated investigation, by checking the recent deployments.
- **11:43 AM** - I started analysing server logs and monitoring data.
- **11:47 AM** - I identified the database server failure due to unexpected traffic spike.
- **11:51 AM** - Additional server capacity was provisioned to restore website functionality.
- **11:54 AM** - Normal website operations were fully restored.

## Root cause and resolution

A sudden increase in user traffic, due to the new marketing campaign, exceeded the server's capacity. The current infrastructure lacked the necessary scalability to handle unexpected traffic spikes. 
With the help of the IT team, we worked promptly to identify and address the root cause, implementing measures to restore website functionality.
- Database queries and performance were optimized to handle increased traffic more efficiently.
- Additional server capacity was provisioned to enhance the website's scalability.

## Corrective and preventative

To prevent similar incidents in the future, here are some recommendations :
- Implement robust traffic monitoring tools to detect sudden spikes in user activity and respond proactively.
- Review and enhance the website's scalability to handle unexpected increases in traffic without service disruption, by implementing automated scaling mechanisms to dynamically adjust server capacity based on traffic patterns.
- Conduct regular and comprehensive load testing to simulate various traffic scenarios and identify potential performance bottlenecks.
