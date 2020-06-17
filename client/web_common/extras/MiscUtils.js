import shortid from 'shortid';
import { NotificationManager } from 'react-notifications';

export default class MiscUtils {

    static generateId() {
        return shortid.generate();
    }


    static setToCookie(key, value, expiredInUTCString) {
        let expires = "";
        if (!expiredInUTCString) {
            const expiredInDays = 1;
            let date = new Date();
            date.setTime(date.getTime() + expiredInDays * 24 * 60 * 60 * 1000);
            expires = "; expires=" + date.toUTCString();
        } else
            expires = "; expires=" + expiredInUTCString;
        document.cookie = key + "=" + (value || "")  + expires + "; path=/";
    }


    static getFromCookie(key, defaultVal) {
        let nameEQ = key + "=";
        let ca = document.cookie.split(';');
        for(let i=0;i < ca.length;i++) {
            let c = ca[i];
            while (c.charAt(0)==' ') c = c.substring(1, c.length);
            if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
        }
        return defaultVal;
    }


    static clearCookie(key) {
        this.setToCookie(key, null, '1970-01-00T00:00:00.000Z')
    }


    static showNotification(message, type) {
        switch (type) {
            case 'error':
                NotificationManager.error(message);
                break;
            default:
                NotificationManager.success(message);
        }
    }


    static showErrorMessage(message) {
        this.showNotification(message, 'error');
    }


    static commonCallbackError(component, error) {
        component.setState({isProcessing: false});
        this.showErrorMessage(error.message);
    }


    static componentChangeInput(component, e, key) {
        let obj = {};
        obj[key] = e.target.value;
        component.setState(obj);
    };

}