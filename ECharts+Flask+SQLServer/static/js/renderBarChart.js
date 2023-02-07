
jQuery(document).ready(() => {
    getChart();
    console.log('Static chart rendered successfully!')
});


let getChart = () => {
    const dom = document.getElementById('container');
    let myChart = echarts.init(dom);
    myChart.showLoading();
    myChart.on('click', function(arg) {
        window.open('https://www.google.com.hk/search?q=' + encodeURIComponent(arg.name));
    });

    const option = {
        title: {
            text: 'ECharts Graph by Python'
        },
        tooltip: {},
        legend: {
            data:['Value']
        },
        xAxis: {
            data: ["shirt", "cardigan", "chiffon", "pants", "high heels", "stockings"]
        },
        yAxis: {},
        series: [{
            name: 'Value',
            type: 'bar',
            data: ["93", "94", "85", 0, null, null, 89, 34],
        }],
        Animation: true,
    };

    myChart.hideLoading();
    myChart.setOption(option);
    console.log(option.series[0].data);
};
