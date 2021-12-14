import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { ConnectedRouter } from 'connected-react-router';

import { createPumpkinStore, history } from './redux/redux-store';
import MainSwitch from "./routing/main-switch";

const pumpkinStore = createPumpkinStore();

function AppController() {
    function render() {
        ReactDOM.render(
            <Provider store={pumpkinStore}>
                <ConnectedRouter history={history}>
                    <MainSwitch />
                </ConnectedRouter>
            </Provider>,
            document.getElementById('root')
        );
    }

    render();
}

export default AppController;
