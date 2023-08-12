import React from 'react'
import {
  MDBFooter,
  MDBContainer,
  MDBIcon,
  MDBBtn
} from 'mdb-react-ui-kit';

const Footer = () => {
  const raiseInvoiceClicked = () => {
    window.open('https://gitlab.com/pioneer22022001/group-1-it5420.git', "_blank")
 }
  return (
    <MDBFooter className='bg-dark text-center text-white'>
      <MDBContainer className='p-4 pb-0'>
        <section className='mb-4'>
          <MDBBtn outline color="light" floating className='m-1' onClick={raiseInvoiceClicked} role='button'>
            <MDBIcon fab icon='github' size='2x' />
          </MDBBtn>
        </section>
      </MDBContainer>

      <div className='text-center p-3' style={{ backgroundColor: 'rgba(0, 0, 0, 0.2)' }}>
        Website: <span />
        <a className='text-white' href='/'>
          trendingposts.com
        </a>
      </div>
    </MDBFooter>
  )
}

export default Footer;