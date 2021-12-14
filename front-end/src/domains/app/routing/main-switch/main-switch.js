import { BrowserRouter as Router, Redirect, Route, Switch } from 'react-router-dom';
import HomePage from "../../view/home-page/home-page";
import Utilization from "../../view/utilization/utilization";

function MainSwitch() {
    return (
        <Router>
            <Switch>
                <Route exact path = "/">
                    <HomePage/>
                </Route>
                <Route exact path = "/utilization">
                    <Utilization/>
                </Route>
            </Switch>
        </Router>

    );
}

export default MainSwitch;
