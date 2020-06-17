import { URLUtils, ADMIN_URL_MAPPING } from '../../../web_common/extras';
import { BACKEND_URL } from '../config';
import ApiHttp from './http';

export default class ApiFeed {

    static create = (callbackSuccess, callbackError, data) => {
        const url = URLUtils.buildAPIURL(BACKEND_URL, ADMIN_URL_MAPPING.FEED.CREATE);
        ApiHttp.post(url, callbackSuccess, callbackError, data);
    };

    static getAll = (callbackSuccess, callbackError, data) => {
        const url = URLUtils.buildAPIURL(BACKEND_URL, ADMIN_URL_MAPPING.FEED.GET_ALL);
        ApiHttp.get(url, callbackSuccess, callbackError, data);
    };

    // static getById = (callbackSuccess, callbackError, data) => {
    //     const url = URLUtils.buildAPIURL(URL_MAPPING.faq.getById);
    //     ApiHttp.get(url, callbackSuccess, callbackError, data);
    // };
    //
    // static delete = (callbackSuccess, callbackError, data) => {
    //     const url = URLUtils.buildAPIURL(URL_MAPPING.faq.delete);
    //     ApiHttp.post(url, callbackSuccess, callbackError, data);
    // };

    static getAllSources = (callbackSuccess, callbackError) => {
        const url = URLUtils.buildAPIURL(BACKEND_URL, ADMIN_URL_MAPPING.FEED.GET_ALL_SOURCES);
        ApiHttp.get(url, callbackSuccess, callbackError);
    };

}