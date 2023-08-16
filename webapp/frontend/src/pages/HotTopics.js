import {React, useEffect, useState} from 'react'
import photo from '../img/headerphoto.png'
import HotTopicCard from '../components/HotTopicCard';
import axios from 'axios';
// import data from '../data_topics.json'

// Hot topics
const HotTopics = () => {
  const [data, setData] = useState([]);
  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      const result = await axios.get("http://localhost:8000/get_hot_topics/");
      // console.log(typeof result.data.topic_names.slice(0, 5));
      setData(result.data.topic_names);
    } catch (error) {
      console.error("Error loading data:", error);
    }
    
  }

  const [selectedOption, setSelectedOption] = useState('10');
  const handleSelectChange = (event) => {
    setSelectedOption(event.target.value);
   
  };
  console.log(data)
  // console.log(data.topic_names)

  const hotTopics = data.slice(0, selectedOption);

  return (
    <>
      <div className='image_wrapper'>
        <img className='img-header' src={photo} alt='header photo'/>
        <div class="overlay overlay_2">
        <h1>What's new today?</h1> 
      </div>
      
      </div>
      <div className='date-picker d-flex'>
        {/* <h7>From </h7>
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
      /> */}
        <h7>Top</h7>
        <select class="form-select input-date" aria-label="Default select example"
                value={selectedOption}
                onChange={handleSelectChange}>
          <option value="10">10</option>
          <option value="15">15</option>
          <option value="20">20</option>
        </select>
      </div>
      <div className='hot-topic-area'>
      {hotTopics.length > 0 ? (
              hotTopics.map((topic, index) => {
                const cleanTopic = topic.replace(/[_+]/g, ' ').trim();
                return (
        <HotTopicCard key={index} topic={cleanTopic} index={index}/>
        );
      })
      ) : (
        <h5>Loading...</h5>
      )} 
      </div>
    </>
  )
}

export default HotTopics