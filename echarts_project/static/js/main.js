// main.js
document.addEventListener("DOMContentLoaded", async () => {
	try {
		// Fetch data from server
		const response = await fetch("/api/sakila-data"); // 从后端获取数据的 API 路径
		// Check for HTTP errors
		if (!response.ok) {
			throw new Error(`Failed to fetch data: ${response.status}`);
		}
		const data = await response.json();
		// Validate data (example, adjust based on your data structure)
		if (!Array.isArray(data.labels) || !Array.isArray(data.values)) {
			throw new Error("Invalid data format received from server.");
		}

		// Initialize ECharts instance
		const myChart = echarts.init(document.getElementById("myChart"));

		// Chart options
		const option = {
			title: {
				text: "My ECharts Demo 1",
				left: "center",
			},
			xAxis: {
				type: "category",
				data: data.labels, // x axis
			},
			yAxis: {
				type: "value",
			},
			series: [
				{
					type: "bar",
					//data: data.map(item => item.value),
					data: data.values, //y axis
				},
			],
		};

		// Apply options
		myChart.setOption(option);
	} catch (error) {
		console.error("Error fetching or processing data:", error);
	}
});
