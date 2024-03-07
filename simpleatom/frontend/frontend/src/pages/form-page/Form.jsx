import { useEffect, useRef } from 'react';
import { ConversationalForm } from 'conversational-form';
import './Form.css';
// import Close from '../../assets/Close_gray.png';
import { useNavigate } from 'react-router-dom';

export const Form = () => {
const Close = "/static/Close_gray.png"

  const navigate = useNavigate();
  let cf = null;
  const ref = useRef(null);

  useEffect(() => {
    cf = ConversationalForm.startTheConversation({
      options: {
        theme: 'dark',
        submitCallback: submitCallback,
        flowStepCallback: flowCallback,
        preventAutoFocus: true,
        loadExternalStyleSheet: true,
      },
      tags: formFields,
    });

    ref.current.appendChild(cf.el);

    return () => {
      cf.remove();
    };
  }, []);

  const submitCallback = () => {
    var formDataSerialized = cf.getFormData(true);
    console.log('Formdata, obj:', formDataSerialized);
    cf.addRobotChatResponse(
      'You are done. Check the dev console for form data output.'
    );
  };

  const flowCallback = function (dto, success, error) {
    //Подгрузка и добавление вопроса сюда
    console.log('dto....', dto, success, error);
    cf.addTags([
      {
        tag: 'input',
        type: 'text',
        name: 'firstname',
        'cf-questions': 'What is your firstname?',
      },
    ]);
    return success();
  };

  const formFields = [
    {
      tag: 'input',
      type: 'text',
      name: 'email',
      'cf-questions': 'What is your email?',
    },
    // {
    //   tag: 'input',
    //   type: 'text',
    //   name: 'firstname',
    //   'cf-questions': 'What is your firstname?',
    // },
    // {
    //   tag: 'input',
    //   type: 'text',
    //   name: 'lastname',
    //   'cf-questions': 'What is your lastname?',
    // },
  ];

  return (
    <div className="form-page">
      <div ref={ref} />
      <p className="closeButton" onClick={() => navigate('/main')}>
        Close
      </p>
    </div>
  );
};
