SELECT meter_id, SUM(usage) AS total_usage
FROM smart_meter_data
GROUP BY meter_id;
