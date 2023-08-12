import {React, useState} from 'react'
import photo from '../img/headerphoto.png'
import top10 from '../img/Component 1.png'
import top5 from '../img/Component 2.png'
import DatePicker from "react-datepicker";
import PostCard from '../components/PostCard';
import Top5Tab from '../components/Top5Tab';



const Home = () => {
  const [date, setDate] = useState(new Date());
  const [startDate, setStartDate] = useState();
  const [endDate, setEndDate] = useState();

  return (
    <>
      <div className='image_wrapper'>
        <img className='img-header' src={photo} alt='header photo'/>
        <div class="overlay overlay_2">
        <h1>What's new today?</h1> 
      </div>
      
      </div>
      <div className='date-picker d-flex'>
        <h7>From </h7>
        <DatePicker
          selectsStart
          selected={startDate}
          onChange={date => setStartDate(date)}
          startDate={startDate}
          className='input-date'
        />
        <h7> to </h7>
        <DatePicker
          selectsEnd
          selected={endDate}
          onChange={date => setEndDate(date)}
          endDate={endDate}
          startDate={startDate}
          minDate={startDate}
          className='input-date'
      />
      </div>
      <div className='row top-posts-container'>
        <div className='col-sm-8 top10-container'>
          <img src={top10} className='top10-title'/>
          <div className='top10-postcard-container'>
            <PostCard />
          </div>
        </div>
        <div className='col-sm-4'>
          <img src={top5} className='top5-title'/>
          <Top5Tab />
        </div>
      </div>
    </>
  )
}

export default Home