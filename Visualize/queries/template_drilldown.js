document.addEventListener('DOMContentLoaded', function () {
    const chart = Highcharts.chart('container', {
        chart: {type: 'column'},
        title: {text: 'Basic Chart with Drilldown'},
        xAxis: {type: 'category'},
        series: [
            {
                name: 'MARK',
                data: [
                    {name: '22-04-2024',y: 5,drilldown: '22-04-2024'},
                    {name: '21-04-2024',y: 2,drilldown: '21-04-2024'},
                    {name: 'Move',y: 4}
                ]
            }
        ],
        drilldown: {
            series: [
                {id: '22-04-2024', data: [['Subcategory 1', 4],['Subcategory 2', 1]]},
                {id: '21-04-2024',data: [['Subcategory 1', 3],['Subcategory 2', 6]]}
            ]
        }
    });
});
