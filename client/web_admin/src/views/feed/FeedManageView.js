import React from "react";
import { Row, Col, InputGroup, InputGroupAddon, Button, Input} from 'reactstrap';
import { DataTable } from '../../components';
import { MiscUtils } from '../../../../web_common/extras';
import { ApiFeed } from '../../api';
import { COOKIE_NAME, DEFAULT_PAGE_SIZE } from '../../config';


export default class FeedManageView extends React.Component{

    state = {
        isProcessing: false,
        pageSize: MiscUtils.getFromCookie(COOKIE_NAME.PAGE_SIZE) ? MiscUtils.getFromCookie(COOKIE_NAME.PAGE_SIZE) : DEFAULT_PAGE_SIZE,
        page: 1,
        filterKeyword: '',
        feeds: []
    }


    changeInput = (e, key) => {
        let obj = {};
        obj[key] = e.target.value;
        this.setState(obj, () => console.log(this.state.filterKeyword));
    };


    onEnterPress = (e) => {
        if(e.keyCode == 13) {
            e.preventDefault();
            // this.saveTalk();
            alert('enter')
        }
    }


    pagerSelectCallback = (page) => {
        this.setState({page}, () => this.getFeeds());
    }


    getFeeds = () => {
        const callbackSuccess = (response) => {
            this.setState({
                isProcessing: false,
                rows: response.feeds
            });
        };
        const callbackError = (error) => {
            MiscUtils.commonCallbackError(this, error);
        };
        this.setState({isProcessing: true}, () => {
            const { pageSize, filterKeyword, page } = this.state;
            const data = {
                page,
                pageSize,
                filterKeyword
            }
            ApiFeed.getAll(callbackSuccess, callbackError, data);
        });
    }


    componentDidMount() {
        this.getFeeds();
    }


    render() {
        return (
            <div>
                <h4 className="paddingVertical20">Feed Management</h4>
                <Row className="paddingVertical20">
                    <Col sm="3" xs="6">
                        <InputGroup>
                            <Input placeholder="Filter by Source"
                                   onChange={(e) => this.changeInput(e, 'filterKeyword')}
                                   onKeyDown={this.onEnterPress}
                            />
                            <InputGroupAddon addonType="append">
                                <Button color="success">Search</Button>
                            </InputGroupAddon>
                        </InputGroup>
                    </Col>
                    <Col sm="9" xs="12">
                        <Button outline color="danger" size="md"  className="pullRight">+ Add</Button>
                    </Col>
                </Row>

                <DataTable pagerSelectCallback={this.pagerSelectCallback}/>

            </div>
        );
    }

}