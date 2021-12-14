import { connectRouter } from 'connected-react-router';
import { combineReducers } from 'redux';

import { appReducer } from '../state';

const RESET = 'RESET';

export default function pumpkinReducer(history) {
    const reducers = combineReducers({
        app: appReducer,
        router: connectRouter(history),
    });

    return (state, action) => {
        const newState =
            action.type === RESET
                ? {
                    router: state.router,
                }
                : state;

        return reducers(newState, action);
    };
}

export function resetStoreState() {
    return { type: RESET };
}
