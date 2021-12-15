import axios from 'axios';

import { BASE_API } from "../constants";
import { setAppClaims, setAppUtilization, incrementClaimedAmount, decrementClaimedAmount, setManageUtilizationTable } from "../state";

const HARD_CODED_DATA = {
    type: 'prevent',
    id: 12620,
    amount_claimed: 800,
    line_items: [
        {
            type: 'Vaccine',
            quantity: 3,
            amount_claimed: 200,
        },
        {
            type: 'Wellness Exams',
            quantity: 1,
            amount_claimed: 200,
        },
        {
            type: 'Blood Test',
            quantity: 2,
            amount_claimed: 200,
        },
        {
            type: 'Fecal "Poop" Test',
            quantity: 1,
            amount_claimed: 200,
        }
    ]
};

var HARD_CODED_UTIL = {
    name: 'Bella',
    birthday: '06/16/2018',
    weight: 16,
    line_items: [
        {
            type: 'Vaccine',
            total: 100,
            remaining: 100,
            utilized: 0
        },
        {
            type: 'Wellness Exams',
            total: 100,
            remaining: 100,
            utilized: 0
        },
        {
            type: 'Blood Test',
            total: 100,
            remaining: 100,
            utilized: 0
        },
        {
            type: 'Fecal "Poop" Test',
            total: 100,
            remaining: 100,
            utilized: 0
        }
    ]
}

export function loadData() {
    return (dispatch) => {
        return axios
            .get(`${BASE_API}/claims`)
            .then((data) => dispatch(setAppClaims(data)));
        // .catch(() => {
        //     dispatch(setAppClaims(some error?));
        // });
        // dispatch(setAppClaims(HARD_CODED_DATA));
    }
}

export function loadUtilizationData(claim_id){
    return (dispatch) => {
        return axios
            .get(`${BASE_API}/claims/` + claim_id + `/utilization`)
            .then((data) => dispatch(setAppUtilization(data)));
    }
}

export const manageUpdateTables = (row, claim_id, value, status) => {
    return (dispatch) => {
        //save row item => save utilization table
        axios.post(`${BASE_API}/claims/update`, {
            id: row.id,
            claim_line_item_type: row.claim_line_item_type,
            quantity: row.quantity,
            decision: value,
            amount_claimed: row.amount_claimed,
            claim_id: claim_id,
            status: status       
        }).then(function (new_updated_util_obj) {
            dispatch(setManageUtilizationTable(row, new_updated_util_obj))
        })
    }
}
