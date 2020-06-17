import React from 'react';
import classnames from 'classnames';
import { Pagination, PaginationItem, PaginationLink } from 'reactstrap';
import { MiscUtils } from '../../../web_common/extras';
import { DATATABLE_PAGER_LENGTH } from '../config';

export default class Pager extends React.Component{

    state = {
        pageList: [],
        currentPage: this.props.page
    };


    renderPager = () => {
        const { currentPage } = this.state;
        const { totalPage } = this.props;
        let lst = [];
        let size = currentPage + DATATABLE_PAGER_LENGTH - 1;
        if (size > totalPage)
            size = totalPage;
        for (let idx=currentPage; idx <= size; idx++)
            lst.push(idx);
        this.setState({pageList: lst});
    };


    changePage = (page) => {
        this.setState({currentPage: page}, () => {
            this.renderPager();
        });
        if (this.props.pagerSelectCallback)
            this.props.pagerSelectCallback(page);
    };


    next = () => {
        const { totalPage } = this.props;
        const { currentPage } = this.state;
        if ( currentPage < totalPage)
            this.changePage(currentPage+1);
    };


    previous = () => {
        const { currentPage } = this.state;
        if ( currentPage >= 2)
            this.changePage(currentPage-1);
    };


    first = () => {
        this.changePage(1);
    };


    last = () => {
        const { totalPage } = this.props;
        this.changePage(totalPage);
    };


    componentDidMount = () => {
        this.renderPager();
    };


    render() {
        const { totalPage } = this.props;
        const { pageList, currentPage } = this.state;

        return (
            <div className="datatablePager">
                {
                    totalPage > 1 &&
                    <Pagination size="sm" className="pullRight">

                        {
                            currentPage > 2 &&
                            <PaginationItem>
                                <PaginationLink first onClick={this.first} />
                            </PaginationItem>
                        }
                        {
                            currentPage !== 1 &&
                            <PaginationItem>
                                <PaginationLink previous onClick={this.previous} />
                            </PaginationItem>
                        }


                        {
                            pageList.map((num, idx) =>
                                <PaginationItem key={MiscUtils.generateId()}>
                                    <PaginationLink onClick={() => {this.changePage(num)}}
                                                    className={classnames({selectedPager: num === currentPage})}
                                    >
                                        {num}
                                    </PaginationLink>
                              </PaginationItem>
                            )
                        }


                        {
                            currentPage < totalPage &&
                            <PaginationItem>
                                <PaginationLink next onClick={this.next} />
                            </PaginationItem>
                        }

                        {
                            currentPage < (totalPage-1) &&
                            <PaginationItem>
                                <PaginationLink last onClick={this.last} />
                            </PaginationItem>
                        }
                    </Pagination>
                }
            </div>
        );
    }
}