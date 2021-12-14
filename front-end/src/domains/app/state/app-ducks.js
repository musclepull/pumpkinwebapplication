const SET_APP_CLAIMS = 'app/SET_APP_CLAIMS';
const MANAGE_UTILIZATION = 'app/MANAGE_UTILIZATION';
const SAVE_UTILIZATION = 'app/SAVE_APP_UTILIZATION';

const appInitialState = {
    claims: null,
    modifiedUtilization: null
};

//banker

//receives action that consists of type and payload: 


export default function appReducer(state = appInitialState, { payload, type, row } = {}) {
    switch (type) {
        case SET_APP_CLAIMS:
            return { ...state, claims: payload };
        case MANAGE_UTILIZATION: {
            var list = [];
            var completeObj = {};
            var r = 1;
            var c = 1;

            completeObj.name = "Bella";
            completeObj.birthday = "06/16/2018";
            completeObj.weight = "16";

            payload.data.data.map(obj => {
                var modifiedUtilization = {};
                modifiedUtilization.claim_line_item_type = obj.claim_line_item_type;
                modifiedUtilization.id = obj.id;
                modifiedUtilization.row_id = "row_" + r;
                modifiedUtilization.col_id = "col_" + r;
                modifiedUtilization.quantity = obj.utilized;
                modifiedUtilization.total = obj.total;
                modifiedUtilization.remaining = obj.total - obj.utilized;
                list.push(modifiedUtilization);
                r++;
                c++;     
            })            

            completeObj.utilObj = list

            return { ...state, modifiedUtilization: completeObj }
        }

        case SAVE_UTILIZATION: {
            var list = [];
            var modifiedUtilization = {};
            var completeObj = {};

            completeObj.name = "Bella";
            completeObj.birthday = "06/16/2018";
            completeObj.weight = "16";

            modifiedUtilization.type = payload.benefit_type;
            modifiedUtilization.utilized = payload.utilized;
            modifiedUtilization.total = payload.total;
            modifiedUtilization.claim_id = payload.claim_id;
            modifiedUtilization.line_item_id = payload.line_item_id;

            completeObj.utilObj = modifiedUtilization

            return { ...state, modifiedUtilization: completeObj }
        }
        default:
            return state;
    }
}

export function setAppClaims(payload) {
    return {
        row: {},
        type: SET_APP_CLAIMS,
        payload,
    };
}

export function setAppUtilization(payload){ 
    return{
        type: MANAGE_UTILIZATION,
        payload,
    }
}

export const setManageUtilizationTable = (row, payload) => ({
    row: row,
    type: SAVE_UTILIZATION,
    payload,
})