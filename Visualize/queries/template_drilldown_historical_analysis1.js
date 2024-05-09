document.addEventListener('DOMContentLoaded', function () {
    const chart = Highcharts.chart('container', {
        chart: {type: 'column'},
        title: {text: 'Basic Chart with Drilldown'},
        xAxis: {type: 'category'},
        
        series: [
            {
                name: '19-04-2024',
                data: [
                    {name: 'MARK',y: 5,drilldown: 'MARK'}
                ]
            },
            {
                name: '20-04-2024',
                data: [
                    {name: 'MARK',y: 7,drilldown: 'MARK'}
                ]
            },
            {
                name: '21-04-2024',
                data: [
                    {name: 'MARK',y: 5,drilldown: 'MARK'}
                ]
            },
            {
                name: '22-04-2024',
                data: [
                    {name: 'MARK',y: 5,drilldown: 'MARK'}
                ]
            },
            {
                name: '23-04-2024',
                data: [
                    {name: 'MARK',y: 5,drilldown: 'MARK'}
                ]
            },
        ],
        
        drilldown: {
            series: [
                {
                    id: 'MARK',
                    name:'SBU',
                    data: [
                        {name: 'EQD_19-04-2024',y:1, drilldown:'EQD'},
                        {name: 'EQD_20-04-2024',y:2, drilldown:'FIC'}
        
                    ]
                }
            ]
        }
    });
});
