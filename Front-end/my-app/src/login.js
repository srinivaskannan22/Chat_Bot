
import 'bootstrap/dist/css/bootstrap.min.css';
import './login.css';

function Login(){
 return(<>
        <h1 class="text-success text-center">
            AI CHATBOT
        </h1>
        <div class="container mt-5">
            <div class="row justify-content-center">
                <div class="col-md-6">
                    <div class="card">
                        <div class="card-body">
                            <form id="registrationForm" action="">
                                <div class="form-group">
                                    <label for="email">
                                        Email
                                    </label>
                                    <input type="email" 
                                        class="form-control" 
                                        id="email" 
                                        placeholder="Email" required />
                                </div>
                                <div class="form-group">
                                    <label for="password">
                                        Password
                                    </label>
                                    <input type="password" 
                                        class="form-control" 
                                        id="password" 
                                        placeholder="Password"
                                        required />
                                </div>
                                <button class="btn btn-danger">
                                    Login
                                </button>
                            </form>
                            <p class="mt-3">
                                Not registered?
                                <a href="#">Create an
                                    account</a>
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
</>
 )

}

export default Login;