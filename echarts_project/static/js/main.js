// main.js
async function fetchData(url) {
	try {
		const response = await fetch(url);
		if (!response.ok) {
			throw new Error(`Failed to fetch data: ${response.status}`);
		}
		return await response.json();
	} catch (error) {
		console.error(`Error fetching data: ${error}`);
		throw error;
	}
}

async function initChart(url) {
	try {
		// Fetch data from server
		const data = await fetchData(url);

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
				data: data.labels,	// x axis
			},
			yAxis: {
				type: "value",
			},
			series: [
				{
					type: "bar",
					//data: data.map(item => item.value),
					data: data.values,	//y axis
				},
			],
		};

		// Apply options
		myChart.setOption(option);
	} catch (error) {
		console.error(`Error fetching or processing data: ${error}`);
	}
}

document.addEventListener("DOMContentLoaded", async () => {
	await initChart("/api/films/all/average_rating");
});
