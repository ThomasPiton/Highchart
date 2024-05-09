document.addEventListener('DOMContentLoaded', function () {
    const chart = Highcharts.chart('container', {
        chart: {type: 'column'},
        title: {text: 'Basic Chart with Drilldown'},
        xAxis: {type: 'category'},
        series: [
            {
                name: 'EQD', 
                type:'line', 
                data: [
                    {name: '19-04-2024',y: 7,drilldown: '19-04-2024_EQD'},
                    {name: '20-04-2024',y: 6,drilldown: '20-04-2024_EQD'},
                    {name: '21-04-2024',y: 1,drilldown: '21-04-2024_EQD'},
                    {name: '22-04-2024',y: 2,drilldown: '22-04-2024_EQD'},
                    {name: '23-04-2024',y: 3,drilldown: '23-04-2024_EQD'}
                ]
            },
            {
                name: 'FIC', 
                type:'line', 
                data: [
                    {name: '19-04-2024',y: 2,drilldown: '19-04-2024_FIC'},
                    {name: '20-04-2024',y: 4,drilldown: '20-04-2024_FIC'},
                    {name: '21-04-2024',y: 5,drilldown: '21-04-2024_FIC'},
                    {name: '22-04-2024',y: 2,drilldown: '22-04-2024_FIC'},
                    {name: '23-04-2024',y: 1,drilldown: '23-04-2024_FIC'}
                ]
            },
            {
                name: 'MGT', 
                type:'line', 
                data: [
                    {name: '19-04-2024',y: 12,drilldown: '19-04-2024_MGT'},
                    {name: '20-04-2024',y: 2,drilldown: '20-04-2024_MGT'},
                    {name: '21-04-2024',y: 1,drilldown: '21-04-2024_MGT'},
                    {name: '22-04-2024',y: 10,drilldown: '22-04-2024_MGT'},
                    {name: '23-04-2024',y: 5,drilldown: '23-04-2024_MGT'}
                ]
            },
        ],
        drilldown: {
            series: [
                {
                    id: '19-04-2024_EQD',
                    name:'EQD',
                    type:'line',
                    data: [
                        {name: '19-04-2024',y: 2,drilldown: '19-04-2024_FIC'},
                        {name: '20-04-2024',y: 4,drilldown: '20-04-2024_FIC'},
                        {name: '21-04-2024',y: 5,drilldown: '21-04-2024_FIC'},
                        {name: '22-04-2024',y: 2,drilldown: '22-04-2024_FIC'},
                        {name: '23-04-2024',y: 1,drilldown: '23-04-2024_FIC'}
                    ]
                },
                {
                    id: '19-04-2024_EQD',
                    name:'FIC',
                    type:'line',
                    data: [
                        {name: '19-04-2024',y: 7,drilldown: '19-04-2024_EQD'},
                        {name: '20-04-2024',y: 6,drilldown: '20-04-2024_EQD'},
                        {name: '21-04-2024',y: 1,drilldown: '21-04-2024_EQD'},
                        {name: '22-04-2024',y: 2,drilldown: '22-04-2024_EQD'},
                        {name: '23-04-2024',y: 3,drilldown: '23-04-2024_EQD'}
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
