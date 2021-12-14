import axios from 'axios';
import { BASE_API } from "../constants";


export default function postData(data) {
    return (dispatch) => {
        return axios
            .post(`${BASE_API}/postUtilization`, data)
            .then(function (response) {
                console.log(response);
            });
    }
}
