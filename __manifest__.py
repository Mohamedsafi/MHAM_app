{


  'name':'Mham App',
  'summary':'To Manage your daily job tasks.',
  'description':"Manage and arrange your daily tasks",
  'author':'Mohamed Safi',
  'depends':['base'],
  'data':['security/ir.model.access.csv',
        'views/todo_task.xml',
          'reports/todo_report.xml',
        ],

   'installable': True,



  }