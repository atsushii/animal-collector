import Routes from "./router/Routes";
import { useRoutes } from "hookrouter";

const App = () => {
    const router = useRoutes(Routes);
    return (
        <div>
            <a href="/signup">Sign Up</a>
            <a href="/login">LogIn</a>            
            <a href="/dashboard">DashBoard</a>
            {router}
        </div>
    )
};

export default App;