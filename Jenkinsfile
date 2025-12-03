pipeline{
  agent any{
    stages{
      stage(build){
        step{
          echo " build application"
          bat " docker build -t mypythonflaskapp "
        }
      }
      stage(run){
        step{
          echo " run application in docker "
          bat " docker rm -t mycontainer || exit 0 "
          bat " docker run -t -p 5000:5000 --name mycontainer mypythonflaskapp "
        }
      }
    }
    post{
      sucess{
        echo" pipeline sucessfull"
      }
      failure{
        echo " pipeline failed "
      }
    }
  }
}
