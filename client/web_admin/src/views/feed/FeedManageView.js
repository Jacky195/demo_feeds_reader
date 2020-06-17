import React from "react";
import { Row, Col, InputGroup, InputGroupAddon, Button, Input} from 'reactstrap';
import { DataTable } from '../../components';
import { BlockingComponent } from '../../../../web_common/components';
import { MiscUtils } from '../../../../web_common/extras';
import { ApiFeed } from '../../api';
import { COOKIE_NAME, DEFAULT_PAGE_SIZE, DATATABLE_HEADER_FEED } from '../../config';


export default class FeedManageView extends React.Component{

    state = {
        isProcessing: false,
        pageSize: MiscUtils.getFromCookie(COOKIE_NAME.PAGE_SIZE) ? MiscUtils.getFromCookie(COOKIE_NAME.PAGE_SIZE) : DEFAULT_PAGE_SIZE,
        page: 1,
        filterKeyword: '',
        feeds: [],
        totalPage: 0
    }


    changeInput = (e, key) => {
        let obj = {};
        obj[key] = e.target.value;
        this.setState(obj);
    };


    onEnterPress = (e) => {
        if(e.keyCode == 13) {
            e.preventDefault();
            this.getFeeds();
        }
    }


    pagerSelectCallback = (page) => {
        this.setState({page}, () => this.getFeeds());
    }

    pageLimitChangeCallback = (pageSize) => {
        MiscUtils.setToCookie(COOKIE_NAME.PAGE_SIZE, pageSize);
        this.setState({
            pageSize,
            totalPage: 0
        }, () => this.getFeeds());
    }


    getFeeds = () => {
        const callbackSuccess = (response) => {
            const {feeds, totalPage} = response;
            setTimeout(() => {
                this.setState({
                isProcessing: false,
                feeds,
                totalPage
            });
            }, 500); //  wait 0.5s, in order to show loading indicator
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
        const { isProcessing, feeds, pageSize, page, totalPage } = this.state;
        return (
            <div>
                <h4 className="paddingVertical20">Feed Management</h4>
                <BlockingComponent isProcessing={isProcessing}>
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

                    <DataTable pageLimitChangeCallback={this.pageLimitChangeCallback}
                               header={DATATABLE_HEADER_FEED} data={feeds}
                               pageSize={pageSize}
                               // pager
                               page={page}
                               totalPage={totalPage}
                               pagerSelectCallback={this.pagerSelectCallback}
                    />
                </BlockingComponent>

            </div>
        );
    }

}