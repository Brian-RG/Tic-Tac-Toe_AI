from flask import Flask, request, redirect, url_for

app=Flask(__name__)

mhtml='''
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <style>
            div{
                margin:auto;
                width: 60%;
                text-align: center;
            }
            td {
                width: 100px;
                height: 100px;
            }
            table {
                margin: 5px auto;
            }
            .vert {
                border-left: 2px solid black;
                border-right: 2px solid black;
            }
            .hori {
                border-top: 2px solid black;
                border-bottom: 2px solid black;
            }

            .Mybtn{
                height: 95%;
                width: 95%;
                border: none;
                outline: none;
                background: none;
            }

        </style>
    </head>
    <body>
        <div>
                <form action='/' method="POST">
            
                    <div class="container">
                                        <table>
                            <tr>
                                <td><button type="submit" class="Mybtn" name="play" value=1> </button></td>
                                <td class="vert"> <button type="submit" class="Mybtn" name="play" value=2></button> </td>
                                <td><button type="submit" class="Mybtn" name="play" value=3></button></td>
                            </tr>
                            <tr>
                                <td class="hori"><button type="submit" class="Mybtn" name="play" value=4></button></td>
                                <td class="vert hori"><button type="submit" class="Mybtn" name="play" value=5></button></td>
                                <td class="hori"><button type="submit" class="Mybtn" name="play" value=6></button></td>
                            </tr>
                            <tr>
                                <td><button type="submit" class="Mybtn" name="play" value=7></button></td>
                                <td class="vert"><button type="submit" class="Mybtn" name="play" value=8></button></td>
                                <td><button type="submit" class="Mybtn" name="play" value=9></button></td>
                            </tr>
                            </table>
                    </div>
                </form>
        </div>

        
            

        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    </body> 
</html>

'''


@app.route('/', methods=['GET'])
def hello():
    return mhtml

@app.route('/', methods=['POST'])
def rec():
    valor=request.form['play']
    print(valor)
    return redirect(url_for('hello'))



if __name__=='__main__':
    app.run()