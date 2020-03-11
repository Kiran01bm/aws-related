## General Notes

1. AWS services send predefined metrics to CloudWatch out of the box.
2. It is also possible to send custom metrics.
3. Every metric can have up to 10 dimensions assigned. 
4. Metrics can be aggregated through so called statistics and CloudWatch offers the following statistics: Minimum, maximum, sum, average, count, and percentiles. 
5. Metric Resolution - In TSDB ex: Store a metric value at 1 minute resolution or 1 second resolution.

### Resolution:
1. High Resolution (1 second) and Standard Resolution (60 seconds)
2. CloudWatch stores it with a resolution of 1 second, and you can read and retrieve it with a period of 1 second, 5 seconds, 10 seconds, 30 seconds, or any multiple of 60 seconds.
3. Currently, only custom metrics that you publish to CloudWatch are available at high resolution.

### Statistics:
1. Statistics can be computed for any time periods between 60-seconds and 1-day. 
2. For high-resolution custom metrics, statistics can be computed for time periods between 1-second and 3-hours.
Note:
If you need availability of metrics longer than these periods, you can use the GetMetricStatistics API to retrieve the datapoints for offline or different storage.

### Retention:
1. 14-days to 15-Months
2. CloudWatch retains metric data as follows:
```
	Data points with a period of less than 60 seconds are available for 3 hours. These data points are high-resolution custom metrics.
	Data points with a period of 60 seconds (1 minute) are available for 15 days
	Data points with a period of 300 seconds (5 minute) are available for 63 days 
	Data points with a period of 3600 seconds (1 hour) are available for 455 days (15 months)
```
Note:
CloudWatch does not support metric deletion. Metrics expire based on the retention schedules described above.

### API Pricing
You can use the GetMetricData API to retrieve as many as 500 different metrics in a single request, with a total of as many as 100,800 data points. 
