document.addEventListener('DOMContentLoaded', function () {
    const chart = Highcharts.chart('container', {
        chart: {type: 'column'},
        title: {text: 'Basic Chart with Drilldown'},
        xAxis: {type: 'category'},
        
        series: [
            {
                name: '21-04-2024',
                data: [
                    {name: 'MARK',y: 7,drilldown: '21-04-2024'}
                ]
            },
            {
                name: '22-04-2024',
                data: [
                    {name: 'MARK',y: 5,drilldown: '22-04-2024'}
                ]
            },
            {
                name: 'Move',
                data: [
                    {name: 'MARK',y: -2,drilldown: 'Move'}
                ]
            }
        ],
        
        drilldown: {
            series: [
                {
                    id: '21-04-2024',
                    name:'21-04-2024',
                    data: [
                        {name: 'EQD',y:1, drilldown:'EQD'},
                        {name: 'FIC',y:2, drilldown:'FIC'}
        
                    ]
                },
                {
                    id: '22-04-2024',
                    name:'22-04-2024',
                    data: [
                        {name: 'EQD',y:2, drilldown:'EQD'},
                        {name: 'FIC',y:4, drilldown:'FIC'}
        
                    ]
                },
                {
                    id: 'Move',
                    name:'Move',
                    data: [
                        {name: 'EQD',y:1, drilldown:'EQD'},
                        {name: 'FIC',y:2, drilldown:'FIC'}
        
                    ]
                }
            ]
        }
    });
});
