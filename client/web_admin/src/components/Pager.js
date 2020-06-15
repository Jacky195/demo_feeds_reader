import React from 'react';
import { Pagination, PaginationItem, PaginationLink } from 'reactstrap';


export default class Pager extends React.Component{


    render() {
        return (
            <Pagination size="sm" className="pullRight">

              <PaginationItem>
                <PaginationLink first href="#" />
              </PaginationItem>

              <PaginationItem>
                <PaginationLink previous href="#" />
              </PaginationItem>

              <PaginationItem>
                <PaginationLink href="#">
                  1
                </PaginationLink>
              </PaginationItem>

              <PaginationItem>
                <PaginationLink href="#">
                  2
                </PaginationLink>
              </PaginationItem>

              <PaginationItem>
                <PaginationLink href="#">
                  3
                </PaginationLink>
              </PaginationItem>

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