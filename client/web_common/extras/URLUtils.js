import axios from 'axios';
import queryString from 'query-string';

export default class URLUtils {

    static makeHttpRequest(methodOriginal, urlOriginal, callbackSuccess, callbackError, data, customHeaders) {
        const method = methodOriginal.toLowerCase();
        let url = urlOriginal;
        let config = {
            method: method,
            url: url
        };
        if (data) {
            const paramsTxt = queryString.stringify(data);
            if (method === 'get')
                config['url'] = url + '?' + paramsTxt;
            else if (method === 'post')
                config['data'] = paramsTxt; // for django backend
        }
        let headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'};
        if (customHeaders)
            headers = customHeaders;
        config['headers'] = headers;
        axios(config).then(
            (res) => {
                const { data } = res;
                if (Array.isArray(data)) {
                    callbackSuccess(data);
                    return;
                }
                if (data.status === 'success')
                    callbackSuccess(data);
                else
                    callbackError(data);
            },
            (err) => {callbackError(err); }
        );
    }

    static buildAPIURL(backendURL, url, paramsDict) {
        let tempURL = backendURL + '/api' + url;
        if (paramsDict)
            tempURL = tempURL + '?' + queryString.stringify(paramsDict);
        return tempURL;
    }


}