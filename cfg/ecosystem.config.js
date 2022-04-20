module.exports = {
    apps:[
        // {
        //     name:"api39",
        //     script:"src/api.py",
        //     interpreter:"venv39/Scripts/python.exe",
        //     instances:1,
        //     exec_mode:"fork",
        //     watch:["src"],    
        //     stop_exit_codes: [0]        
            
        // },
        {
            name:"job39",
            script:"src/main.py",
            interpreter:"venv39/Scripts/python.exe",
            instances:1,
            exec_mode:"fork",
            cron_restart:"*/1 * * * *",
            autorestart: false,
            watch:false,    
            stop_exit_codes: [0]        
        },
        {
            name:"job310",
            script:"src/main.py",
            interpreter:"venv310/Scripts/python.exe",
            instances:2,
            exec_mode:"fork", //"cluster",
            cron_restart:"*/1 * * * *",
            autorestart: false,
            watch:false,    
            stop_exit_codes: [0]        
        }
    ]
}