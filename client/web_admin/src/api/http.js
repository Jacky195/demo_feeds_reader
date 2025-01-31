import { URLUtils } from '../../../web_common/extras';

export default class ApiHttp {

    static method(method, url, callbackSuccess, callbackError, data) {
        URLUtils.makeHttpRequest(method, url, callbackSuccess, callbackError, data);
    }

    static get(url, callbackSuccess, callbackError, data) {
        this.method('get', url, callbackSuccess, callbackError, data);
    }

    static post(url, callbackSuccess, callbackError, data) {
        this.method('post', url, callbackSuccess, callbackError, data);
    }

    static put(url, callbackSuccess, callbackError, data) {
        this.method('put', url, callbackSuccess, callbackError, data);
    }

    static delete(url, callbackSuccess, callbackError, data) {
        this.method('delete', url, callbackSuccess, callbackError, data);
    }

}