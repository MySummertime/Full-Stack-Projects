
// ---------------------------------------constant---------------------------------------------
const dom = document.getElementById("container");
let myChart = echarts.init(dom);

// ---------------------------------------functions----------------------------------------------

function initChart() {
    myChart.showLoading();
    myChart.on('click', function(arg) {
        window.open('https://www.google.com.hk/search?q=' + encodeURIComponent(arg.name));
    });
    window.addEventListener("resize", function () {
        myChart.resize();
    });
    console.log("Chart initialized.")
}

// fetch data from json
function fetchJsonData() {
    let ans = $.get("/api/async/draw", (res) => {
        console.log(res.data);
    });
    return ans;
}

async function asyncRender() {
    try {
        let json = await fetchJsonData();
        console.log(json);

        const option = {
            title: {
                text: 'ECharts Graph by Python',
                left: 'center',
            },
            // generate a toolbox
            toolbox: {
                show: true,
                orient: 'vertical',
                left: 'right',
                top: 'center',
                feature: {
                    dataZoom: {
                        yAxisIndex: "none"
                    },
                    dataView: {
                        readOnly: false
                    },
                    // generate types that can be operated dynamically
                    magicType: {
                        type: ['line','bar']
                    },
                    restore: {},
                    saveAsImage: {}
                }
            },
            // produce a legend
            legend: {
                orient: 'vertical',
                left: 'right',
                data: ['Value']
            },
            xAxis: {
                name: "Month",
                data: ['OCT', 'NOV', 'DEC', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP']
            },
            yAxis: {
                name: "Value",
            },
            series: [{
                name: 'Value',
                type: 'bar',
                data: json.data,
            }],
            Animation: true,
        };

        myChart.hideLoading();
        if (option && typeof option === "object") {
            myChart.setOption(option);
        };

        console.log("Chart rendered.");

        // refresh every 10 seconds
        setTimeout(asyncRender, 10000);
    }
    catch (e) {
        console.error(`Couldn't render chart: ${e}`);
        alert("Something went wrong...");
    }
}




jQuery(document).ready(() => {
    initChart();
    asyncRender();
});
