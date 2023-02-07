

// generate an echarts instance
let dom = document.getElementById('container');
let myChart = echarts.init(dom);

// configure the echarts graph
const option = {
    title: {
        text: 'ECharts Graph by node.js'
    },
    tooltip: {},
    legend: {
        data: ['Amount']
    },
    xAxis: {
        data: ['Shirts', 'Cardigan', 'Chiffon Shirts', 'Pants', 'High heels', 'Stockings']
    },
    yAxis: {},
    series: [
        {
            name: 'Amount',
            type: 'bar',
            data: [5, 20, 36, 10, null, 20],
        }
    ]
};


function initChart() {
    try {
        myChart.showLoading();
        myChart.on('click', (arg) => {
            window.open('https://www.google.com.hk/search?q=' + encodeURIComponent(arg.name));
        });
        window.addEventListener("resize", () => {
            myChart.resize();
        });
        console.log("Chart initialized.");
        return true;
    }
    catch (e) {
        console.error(e);
        return false;
    }
}

async function asyncRender() {
    try {
        let flag = await initChart();
        if (!flag) {
            console.log("Chart initialization failed.");
            return;
        }
        myChart.hideLoading();
        myChart.setOption(option);
        console.log("Chart rendered asynchronously.");
    }
    catch (e) {
        console.error(e);
    }
}


jQuery(document).ready(() => {
    asyncRender();
});
