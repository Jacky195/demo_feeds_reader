import React from 'react';
import { Pagination, PaginationItem, PaginationLink } from 'reactstrap';
import { MiscUtils } from '../../../web_common/extras';


export default class Pager extends React.Component{

    render() {
        const { pagerSelectCallback } = this.props;
        const num_list = [1, 2,3];
        return (
            <Pagination size="sm" className="pullRight">

              <PaginationItem>
                <PaginationLink first href="#" />
              </PaginationItem>

              <PaginationItem>
                <PaginationLink previous href="#" />
              </PaginationItem>

                {
                    num_list.map((num, idx) =>
                        <PaginationItem key={MiscUtils.generateId()}>
                            <PaginationLink onClick={() => pagerSelectCallback(num)}>
                                {num}
                            </PaginationLink>
                      </PaginationItem>
                    )
                }


              <PaginationItem>
                <PaginationLink next href="#" />
              </PaginationItem>

              <PaginationItem>
                <PaginationLink last href="#" />
              </PaginationItem>

            </Pagination>
        );
    }

}