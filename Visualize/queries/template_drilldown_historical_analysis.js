document.addEventListener('DOMContentLoaded', function () {
    const chart = Highcharts.chart('container', {
        chart: {type: 'column'},
        title: {text: 'Basic Chart with Drilldown'},
        xAxis: {type: 'category'},
        plotOptions: {
            bar: {
                borderRadius: '5%',
                dataLabels: {
                    enabled: true
                },
                groupPadding: 0.1,
                
            },
            column: {
                borderWidth: 0,
                dataLabels: {
                    enabled: true,
                    format: '{point.y:.1f}%'
                }
            }
        },
        series: [
            {
                name: '19-04-2024',
                data: [
                    {name: 'MARK',y: 5,drilldown: '19-04-2024'}
                ]
            },
            {
                name: '20-04-2024',
                data: [
                    {name: 'MARK',y: 7,drilldown: '20-04-2024'}
                ]
            },
            {
                name: '21-04-2024',
                data: [
                    {name: 'MARK',y: 5,drilldown: '21-04-2024'}
                ]
            },
            {
                name: '22-04-2024',
                data: [
                    {name: 'MARK',y: 5,drilldown: '22-04-2024'}
                ]
            },
            {
                name: '23-04-2024',
                data: [
                    {name: 'MARK',y: 5,drilldown: '23-04-2024'}
                ]
            },
        ],
        
        drilldown: {
            series: [
                {
                    id: '19-04-2024',
                    name:'19-04-2024',
                    data: [
                        {name: 'EQD',y:1, drilldown:'19-04-2024_EQD'},
                        {name: 'FIC',y:2, drilldown:'19-04-2024_FIC'}
        
                    ]
                },
                {
                    id: '20-04-2024',
                    name:'20-04-2024',
                    data: [
                        {name: 'EQD',y:1, drilldown:'20-04-2024_EQD'},
                        {name: 'FIC',y:2, drilldown:'20-04-2024_FIC'}
        
                    ]
                },
                {
                    id: '21-04-2024',
                    name:'21-04-2024',
                    data: [
                        {name: 'EQD',y:1, drilldown:'21-04-2024_EQD'},
                        {name: 'FIC',y:2, drilldown:'21-04-2024_FIC'}
        
                    ]
                },
                {
                    id: '22-04-2024',
                    name:'22-04-2024',
                    data: [
                        {name: 'EQD',y:2, drilldown:'22-04-2024_EQD'},
                        {name: 'FIC',y:4, drilldown:'22-04-2024_FIC'}
        
                    ]
                },
                {
                    id: '23-04-2024',
                    name:'23-04-2024',
                    data: [
                        {name: 'EQD',y:2, drilldown:'23-04-2024_EQD'},
                        {name: 'FIC',y:4, drilldown:'23-04-2024_FIC'}
        
                    ]
                },
                {id: '19-04-2024_EQD',type:"bar", name:'19-04-2024',data: [{name: 'Desk1_EQD',y:2, drilldown:'23-04-2024_EQD'},{name: 'Desk2_EQD',y:4, drilldown:'23-04-2024_FIC'}]},
                {id: '20-04-2024_EQD',type:"bar", name:'20-04-2024',data: [{name: 'Desk1_EQD',y:1, drilldown:'23-04-2024_EQD'},{name: 'Desk2_EQD',y:4, drilldown:'23-04-2024_FIC'}]},
                {id: '21-04-2024_EQD',type:"bar", name:'21-04-2024',data: [{name: 'Desk1_EQD',y:21, drilldown:'23-04-2024_EQD'},{name: 'Desk2_EQD',y:4, drilldown:'23-04-2024_FIC'}]},
                {id: '22-04-2024_EQD',type:"bar", name:'22-04-2024',data: [{name: 'Desk1_EQD',y:2, drilldown:'23-04-2024_EQD'},{name: 'Desk2_EQD',y:4, drilldown:'23-04-2024_FIC'}]},
                {id: '23-04-2024_EQD',type:"bar", name:'23-04-2024',data: [{name: 'Desk1_EQD',y:3, drilldown:'23-04-2024_EQD'},{name: 'Desk2_EQD',y:4, drilldown:'23-04-2024_FIC'}]},

                {id: '19-04-2024_FIC',name:'19-04-2024',data: [{name: 'EQD',y:2, drilldown:'23-04-2024_EQD'},{name: 'FIC',y:4, drilldown:'23-04-2024_FIC'}]},
                {id: '20-04-2024_FIC',name:'20-04-2024',data: [{name: 'EQD',y:2, drilldown:'23-04-2024_EQD'},{name: 'FIC',y:4, drilldown:'23-04-2024_FIC'}]},
                {id: '21-04-2024_FIC',name:'21-04-2024',data: [{name: 'EQD',y:2, drilldown:'23-04-2024_EQD'},{name: 'FIC',y:4, drilldown:'23-04-2024_FIC'}]},
                {id: '22-04-2024_FIC',name:'22-04-2024',data: [{name: 'EQD',y:2, drilldown:'23-04-2024_EQD'},{name: 'FIC',y:4, drilldown:'23-04-2024_FIC'}]},
                {id: '23-04-2024_FIC',name:'23-04-2024',data: [{name: 'EQD',y:2, drilldown:'23-04-2024_EQD'},{name: 'FIC',y:4, drilldown:'23-04-2024_FIC'}]},
      
                
            ]
        }
    });
});
